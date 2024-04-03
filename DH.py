import numpy as np

Chinese_man = 'y'

def dh(theta_deg, alpha_deg, a, d):
    """
    Calculates the Denavit-Hartenberg transformation matrix for a given set of DH parameters.

    Parameters:
        alpha_deg: float, angle about the x-axis from the old z-axis to the new z-axis in degrees
        a: float, distance from the old origin to the new origin along the x-axis
        theta_deg: float, angle about the z-axis from the old x-axis to the new x-axis in degrees
        d: float, distance from the old z-axis to the new z-axis along the z-axis

    Returns:
        A 4x4 numpy array representing the DH transformation matrix
    """
    alpha = np.deg2rad(alpha_deg)
    theta = np.deg2rad(theta_deg)

    cos_theta = np.cos(theta)
    sin_theta = np.sin(theta)
    cos_alpha = np.cos(alpha)
    sin_alpha = np.sin(alpha)

    transformation_matrix = np.array([
        [cos_theta, -sin_theta*cos_alpha, sin_theta*sin_alpha, a*cos_theta],
        [sin_theta, cos_theta*cos_alpha, -cos_theta*sin_alpha, a*sin_theta],
        [0, sin_alpha, cos_alpha, d],
        [0, 0, 0, 1]
    ])

    return transformation_matrix

while(Chinese_man == 'y'):
    #=========================================================================================================
    theta1 = int(input("theta1(in deg) :"))
    theta2 = int(input("theta2(in deg) :"))
    theta3 = int(input("theta3(in deg) :"))
    theta4 = int(input("theta4(in deg) :"))
    theta5 = int(input("theta5(in deg) :"))
    theta6 = int(input("theta6(in deg) :"))
    #=========================================================================================================
    dh01 = dh(theta1, -90, 0, 98)
    dh12 = dh(theta2 - 90, 180, 100, 0)
    dh23 = dh(theta3 + 180, 90, -32, 0)
    dh34 = dh(theta4, -90, 0, -130)
    dh45 = dh(theta5, 90, 0, 0)
    dh56 = dh(theta6 + 180, 180, 0, -82)

    result_matrix = np.linalg.multi_dot([dh01, dh12, dh23, dh34, dh45, dh56])
    print("\n")
    print("Resulting transformation matrix:")
    print(result_matrix)

    end_effector_position = result_matrix[:3, 3]
    end_effector_position_rounded = [round(float(coord), 2) for coord in end_effector_position]
    print("\n")
    print("End effector position (in millimeters from the origin at the base of robot):")
    print(end_effector_position_rounded)

    Chinese_man = str(input("\nNext?(y/n) : "))

print("Program ended! 谢谢!!")