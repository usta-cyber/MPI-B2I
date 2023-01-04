from mpi4py import MPI

# Get the size of the communicator
size = MPI.COMM_WORLD.size

# Print the size of the communicator
print(f"The maximum number of processes that can run is {size}")