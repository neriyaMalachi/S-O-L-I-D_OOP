from S_single_responsibility.single_responsibility import good_Function_S, bad_Function_S
from O_open_closed.bad.open_closed import bad_Function_O
from O_open_closed.good.classes.ManagerBonus import ManagerBonus
from O_open_closed.good.open_closed import good_Function_O
from L_liskov_substitution.bad.liskov_substitution import bad_Function_L
from L_liskov_substitution.good.liskov_substitution import good_Function_L
from I_interface_segregation.bad.interface_segregation import bad_Function_I
from I_interface_segregation.good.interface_segregation import good_Function_I
from D_dependency_inversion.bad.dependency_inversion import bad_Function_D
from D_dependency_inversion.good.dependency_inversion import good_Function_D

# S
print("=== S: Single Responsibility ===")
print("-- GOOD --")
good_Function_S()
print("-- BAD --")
bad_Function_S()
print("\n")

# O
print("=== O: Open/Close ===")
print("-- BAD --")
bad_Function_O()
print("-- GOOD --")
good_Function_O()
print("\n")

# L
print("=== L: Liskov Substitution ===")
print("-- BAD --")
bad_Function_L()
print("-- GOOD --")
good_Function_L()
print("\n")

# I
print("=== I: Interface Segregation ===")
print("-- BAD --")
bad_Function_I()
print("-- GOOD --")
good_Function_I()
print("\n")

# D
print("=== D: Dependency Inversion ===")
print("-- BAD --")
bad_Function_D()
print("-- GOOD --")
good_Function_D()
print("\n")
