from Loading import ft_tdqm
from time import sleep
from tqdm import tqdm

for elem in ft_tdqm(range(50, 333)):
    sleep(0.05)

for elem in tqdm(range(50, 333)):
    sleep(0.05)
