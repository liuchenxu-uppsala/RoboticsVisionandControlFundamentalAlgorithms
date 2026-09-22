# 第2章复习:Representing Position and Orientation

---

## 2.1 Foundations

- **位姿(pose)= 位置(position)+ 姿态(orientation)**
- 书里用运动符号 ξ(motion),组合用 ⊕,求逆用 ⊖,零运动 ∅ —— 概念上等价于我们的 T(矩阵)、连乘(·)、求逆(T⁻¹)、单位矩阵 I
- 这套系统构成"群"(封闭性、结合律、单位元、逆元),但**不满足交换律**
- **位姿图(pose graph)**:多个坐标系用图表示,求未知边 = 找两条起点终点相同的路径,列等式反解(和 WARA 项目里 base/camera/object/gripper 场景高度对应)
- **参考系规则**:组合表达式里,上下标必须"首尾相接"才能消掉中间项 —— 就是我们反复用的"下标相消"

---

## 2.2 Working in 2D

### 2.2.1 旋转(SO(2))
```python
rot2(θ)      # 2x2 纯旋转矩阵
```
- 正交矩阵:每列单位长度、两两垂直;R⁻¹ = Rᵀ;det(R) = 1
- **矩阵指数/对数**:反对称矩阵的指数 = 旋转矩阵
```python
skew(w)      # 数字 -> 反对称矩阵
vex(M)       # 反对称矩阵 -> 数字
scipy.linalg.expm() / logm()
```

### 2.2.2 位姿(SE(2))
```python
trot2(θ, 'deg')     # 3x3 齐次变换,只含旋转
transl2(x, y)        # 3x3 齐次变换,只含平移
trplot2(T)            # 画出2D坐标系
```
- 组合不满足交换律:`transl2(a,b) @ trot2(θ) ≠ trot2(θ) @ transl2(a,b)`
- **矩阵作用在点上时,离点最近的(最右边)先发生**(固定坐标系语义)
- **绕任意点 C 旋转**(共轭 conjugation):
```python
T = transl2(C) @ trot2(θ) @ transl2(-C)
```
- **2D 旋量(Twist2)**:用一个3维向量 (v, ω) 描述"绕哪个点、转多少"
```python
Twist2.UnitRevolute(C)      # 旋转型,绕点C
Twist2.UnitPrismatic(dir)   # 平移型,沿某方向
S.exp(θ)                     # 还原成完整变换矩阵(注意:弧度制!)
S.pole                        # 反推旋转中心
```

---

## 2.3.1 三维姿态表示法(六种方式,描述同一件事)

### 2.3.1.1 3D 旋转矩阵(SO(3))
- 和2D完全同规律,只是3x3;`^A R_B` = B的三根轴在A系下的方向

### 2.3.1.2 欧拉角 / RPY(三角度表示)
- **欧拉旋转定理**:任意姿态差 = 最多3次转动,但不能连续两次绕同一根轴
- 12种序列分两类:重复轴(欧拉角,如ZYZ、ZXZ)/ 三轴都不同(卡尔丹角/RPY,如XYZ、ZYX)
```python
eul2r(φ, θ, ψ)              # 固定用ZYZ顺序
tr2eul(R)                     # 反解ZYZ角度

rpy2r(roll, pitch, yaw, order="xyz")  # 参数永远是(roll,pitch,yaw)!
tr2rpy(R, order="xyz")
```
- ⚠️ **`rpy2r` 参数与轴对应关系(已用源码验证,固定系语义)**:
  - `order="xyz"`: R = rotx(**yaw**) @ roty(pitch) @ rotz(**roll**) —— 参数是反着塞入连乘式的
  - `order="zyx"`: R = rotz(**yaw**) @ roty(pitch) @ rotx(**roll**)
  - `order="yxz"`: R = roty(**yaw**) @ rotx(pitch) @ rotz(**roll**)
  - 规律:`order`字符串从左到右,对应连乘从左到右;**最左边的函数拿最后一个参数(yaw),最右边的函数拿第一个参数(roll)**
  - **只支持这三种 order**,其余顺序(如YXY、XZX等)必须自己手动拼 `rotx()@roty()@rotz()...`

### 2.3.1.3 奇异性与万向节死锁(Gimbal Lock)
- pitch = ±90° 时,roll 和 yaw 耦合成一个自由度,只能确定两者的差值,无法分别反解
- 本质和 Jacobian 奇异性是同一件事:某个映射在特定点上"降秩"、丢失一个独立方向
- 验证:`rpy2r(0.2, 90°, 0.1)` 和 `rpy2r(0.5, 90°, 0.4)`(差值相同)算出同一个矩阵

### 2.3.1.4 双向量表示法(Two-Vector)—— 对夹爪姿态设计最直接
- 接近向量 â(Z轴,夹爪伸出方向)+ 方向向量 ô(Y轴,两指连线方向)
- 第三轴叉乘得到:n̂ = ô × â
```python
oa2r(o, a)     # 直接构造旋转矩阵,不用先换算角度
```

### 2.3.1.5 角轴表示法(Angle-Axis)
- 任意姿态差 = 绕**一根**轴转一个角度
```python
tr2angvec(R)          # 矩阵 -> (角度, 轴)
angvec2r(θ, axis)      # (角度, 轴) -> 矩阵
```
- 常用来衡量"两个姿态差多远"(θ 的大小),用于轨迹规划里评估姿态调整幅度

### 2.3.1.6 矩阵指数(3D 反对称矩阵)
- 反对称矩阵本质:把角速度向量 ω=(ωx,ωy,ωz) 重新排列进3x3矩阵,使得 **[ω]× · p = ω × p**(把叉乘变成矩阵乘法)
```python
def skew(w):
    wx, wy, wz = w
    return np.array([[0,-wz,wy],[wz,0,-wx],[-wy,wx,0]])
```
- 两大用途:
  1. **生成任意轴的旋转矩阵**:`R = expm(θ * skew(axis_unit))`,标准 rotx/roty/rotz 做不到"任意斜轴"时必须用这个
  2. **把 Jacobian 公式里的叉乘,改写成矩阵乘法**:`J_v,i = skew(z_{i-1}) @ (p_n - p_{i-1})`,等价于原来的 `np.cross(z_{i-1}, p_n-p_{i-1})`

### 2.3.1.7 单位四元数(Unit Quaternion)
- 4个数:q = (s, v) = (cos(θ/2), v̂·sin(θ/2)) —— s编码"转多少",v编码"绕哪转+转多少"
- 单位元(不转)= (1,0,0,0)
```python
UnitQuaternion.AngVec(θ, axis)   # 用角度+轴直接构造(最常用)
q1 * q2          # Hamilton乘法(组合两次旋转,对应书里符号∘),不满足交换律
q.inv()          # 求逆(共轭)
q * p_vector      # 变换一个点,内部自动完成 q∘p̄∘q* 三步
q.R               # 转换回3x3旋转矩阵
```
- 优势:无万向节死锁;计算效率更高(相乘16乘12加 vs 矩阵27乘18加)
- ⚠️ **顺序陷阱**:spatialmath顺序是 (s,vx,vy,vz);**ROS消息顺序是 (vx,vy,vz,s/w)!** 往ROS消息塞四元数时必须手动倒换顺序

---

## 2.3.2 三维位姿(SE(3))
```python
transl(x, y, z)              # 4x4,只含平移
trotx(θ,'deg') / troty / trotz   # 4x4,只含旋转(绕标准轴)
trplot(T)                     # 画3D坐标系
```
- 结构和2D完全一致,只是4x4:`T = [[R, t],[0,1]]`
- 命名规律:**函数名带"t"前缀 = 4x4(或2D下3x3)齐次变换矩阵;不带"t" = 纯旋转/纯平移的低一维矩阵**
- `rotx/roty/rotz`只能绕标准坐标轴;绕任意轴必须用 `angvec2r` 或 `UnitQuaternion.AngVec`

---

## 全程反复验证过的核心规则(不要忘)

1. **矩阵作用在点上**:`T @ p`,离 p 最近(最右边)的矩阵先发生 —— 对应"固定坐标系"语义
2. **动坐标系语义**(相对每一步转完后的新坐标系操作):顺序和物理发生顺序**一致**,先发生的写**左边**(和上面规则相反,题目必须先说明是哪种场景!)
3. `@` 是矩阵乘法,`*` 在 numpy 数组上是逐元素相乘(容易踩坑),但在 `UnitQuaternion`/`SE3` 等类上被重载成各自的组合运算
4. `np.allclose` 而不是 `==`,因为浮点数有精度误差
5. 角度参数默认单位是**弧度**,除非函数显式支持 `'deg'` 参数或你自己用 `np.deg2rad()` 转换
