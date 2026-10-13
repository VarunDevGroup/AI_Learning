import time
import asyncio

from timeit import default_timer as timer 

async def run_task(taskname, seconds):
    print(f'{taskname} has started at {timer()}')
    await asyncio.sleep(seconds)
    print(f'{taskname} has emded at {timer()}')

async def main():
    start_time=timer()

    await asyncio.gather(
        run_task('Task 1',2),
        run_task('Task 2',5),
        run_task('Task 3',8)
    )

    print(f'Total time : {timer()-start_time:.2f}s')    

asyncio.run(main())