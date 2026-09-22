"""
3.1.1 - Rate of Change of Rotation Matrix 练习
验证: R_dot = R @ [omega_B]_x  (B系/物体自身视角角速度)
验证: R_dot = [omega_A]_x @ R  (A系/外部世界视角角速度)
"""

import numpy as np

def rotz(t):
    c, s = np.cos(t), np.sin(t)
    return np.array([[c, -s, 0], [s, c, 0], [0, 0, 1]])

def rotx(t):
    c, s = np.cos(t), np.sin(t)
    return np.array([[1, 0, 0], [0, c, -s], [0, s, c]])

def skew(w):
    wx, wy, wz = w
    return np.array([[0, -wz, wy], [wz, 0, -wx], [-wy, wx, 0]])

def vex3(M):
    return np.array([M[2, 1], M[0, 2], M[1, 0]])


print("=" * 50)
print("第一部分:简单情况,绕单一轴转动")
print("=" * 50)

# R(t) = Rz(2t),角速度应该是恒定的2 rad/s,绕Z轴
def R_simple(t):
    return rotz(2 * t)

t = 0.5
dt = 1e-6
R_t = R_simple(t)
R_dot = (R_simple(t + dt) - R_t) / dt

omega_B = vex3(R_t.T @ R_dot)
omega_A = vex3(R_dot @ R_t.T)

print("B系角速度:", omega_B)
print("A系角速度:", omega_A)
print("两者相同吗(绕单轴转动时应该相同):", np.allclose(omega_A, omega_B))


print()
print("=" * 50)
print("第二部分:复杂情况,两个轴同时转动,转速不同")
print("=" * 50)

# R(t) = Rz(t) @ Rx(2t)
def R_complex(t):
    return rotz(t) @ rotx(2 * t)

R_t2 = R_complex(t)
R_dot2 = (R_complex(t + dt) - R_t2) / dt

omega_B2 = vex3(R_t2.T @ R_dot2)
omega_A2 = vex3(R_dot2 @ R_t2.T)

print("B系角速度(物体自身/陀螺仪视角):", omega_B2)
print("A系角速度(外部世界视角):", omega_A2)
print("两者相同吗(复杂转动时不应相同):", np.allclose(omega_A2, omega_B2))


print()
print("=" * 50)
print("第三部分:反过来验证公式本身")
print("=" * 50)

# 验证: R_dot = R @ [omega_B]_x
R_dot_check_B = R_t2 @ skew(omega_B2)
print("用 R @ [omega_B]_x 重新算出的R_dot,和数值求导一致吗?",
      np.allclose(R_dot_check_B, R_dot2, atol=1e-4))

# 验证: R_dot = [omega_A]_x @ R
R_dot_check_A = skew(omega_A2) @ R_t2
print("用 [omega_A]_x @ R 重新算出的R_dot,和数值求导一致吗?",
      np.allclose(R_dot_check_A, R_dot2, atol=1e-4))