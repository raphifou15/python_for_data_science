# def ft_tqdm(lst: range) -> None:
import sys

# import time


def ft_tdqm(lst: range):
    print("")
    sizeLst = len(lst)
    bar = " " * 50
    pourcent = 0
    progress = 0
    i = 0
    last = 0
    for index, elem in enumerate(lst):
        # start_time = time.time()
        yield elem

        progress += 1
        pourcent = int(progress / sizeLst * 100)
        if pourcent % 2 == 0 and last != pourcent:
            tempList = list(bar)
            last = pourcent
            tempList[i] = "█"
            bar = "".join(tempList)
            i += 1
        # elapsed_time = time.time() - start_time
        # if elapsed_time > 0:
        #     it_per_second = 1 / elapsed_time
        pourcent_str = str(pourcent)
        if len(pourcent_str) == 2:
            pourcent_str = " " + pourcent_str
        elif len(pourcent_str) == 1:
            pourcent_str = "  " + pourcent_str
        # res_time = (sizeLst - index) / it_per_second
        # time_did = (index) / it_per_second

        # minutes_rest = int(res_time) // 60
        # secondes_rest = int(res_time) % 60

        # minutes_did = int(time_did) // 60
        # secondes_did = int(time_did) % 60
        # time_rest = "{:02d}:{:02d}".format(minutes_rest, secondes_rest)
        # format_time_did = "{:02d}:{:02d}".format(minutes_did, secondes_did)
        text = f"{pourcent_str}%|{bar}|{progress}/{sizeLst}  "

        # [\
        # {format_time_did}<{time_rest}, {it_per_second:.2f} it/s]
        sys.stdout.write("\033[F")

        sys.stdout.flush()
        print(text)
    return


# for elem in tqdm(range(5000)):
#     sleep(0.0005)

# print()
# print("lala")
