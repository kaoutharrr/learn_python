import time
import asyncio

async def brewCoefee():
    print('start brew coefee()')
    await asyncio.sleep(3)
    print('end brew coefee()')
    return "coeffeeready"

async def toastBagel():
    print("start toast bagel")
    await asyncio.sleep(2)
    print("end toast bagel")
    return "taost readyy"

def normal_main():
    start_time = time.time()
    resultCoffee = brewCoefee()
    resultToast = toastBagel()
    end_time = time.time()
    elapsed_time = end_time - start_time

    print(f"result of coeffee= {resultCoffee}")
    print(f"result of taost = {resultToast}")
    print(f"elapsed time = {elapsed_time}")

async def main_with_batch():
    start_time = time.time()
    batch = asyncio.gather(brewCoefee(),toastBagel())
    resultCoffee,resultToast = await batch

    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"result of coeffee= {resultCoffee}") 
    print(f"result of taost = {resultToast}")
    print(f"elapsed time = {elapsed_time:.2f}")



# main with create task
async def main():
    start_time = time.time()
    coffee_task = asyncio.create_task(brewCoefee())
    toast_task = asyncio.create_task(toastBagel())

    resultCoffee = await coffee_task
    resultToast = await toast_task

    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"result of coeffee= {resultCoffee}") 
    print(f"result of taost = {resultToast}")
    print(f"elapsed time = {elapsed_time:.2f}")
if __name__ == "__main__":
    # main()
    asyncio.run(main())