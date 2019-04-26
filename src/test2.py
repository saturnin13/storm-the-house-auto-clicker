import time

import cv2
import mss
import numpy


with mss.mss() as sct:
    # Part of the screen to capture
    monitor = {"top": 540, "left": 540, "width": 500, "height": 225}

    start = time.time()

    screen = numpy.array(sct.grab(monitor))

    end = time.time()
    print(end - start)

    print(screen.shape)

    screen = cv2.cvtColor(screen, cv2.COLOR_BGR2GRAY)

    cv2.imshow("screen", screen)
    cv2.waitKey()

    # while "Screen capturing":
    #     last_time = time.time()
    #
    #     # Get raw pixels from the screen, save it to a Numpy array
    #     img = numpy.array(sct.grab(monitor))
    #
    #     # Display the picture
    #     cv2.imshow("OpenCV/Numpy normal", img)
    #
    #     # Display the picture in grayscale
    #     # cv2.imshow('OpenCV/Numpy grayscale',
    #     #            cv2.cvtColor(img, cv2.COLOR_BGRA2GRAY))
    #
    #     print("fps: {}".format(1 / (time.time() - last_time)))
    #
    #     # Press "q" to quit
    #     if cv2.waitKey(25) & 0xFF == ord("q"):
    #         cv2.destroyAllWindows()
    #         break

# from multiprocessing import Process, Queue
#
# import mss
# import mss.tools
# import time
#
# from PIL import Image
#
#
# def grab(queue):
#     # type: (Queue) -> None
#
#     rect = {"top": 0, "left": 0, "width": 600, "height": 800}
#
#     with mss.mss() as sct:
#         for _ in range(1_0):
#             queue.put(sct.grab(rect))
#
#     # Tell the other worker to stop
#     queue.put(None)
#
#
# def save(queue):
#     # type: (Queue) -> None
#
#     number = 0
#     output = "file_{}.png"
#     to_png = mss.tools.to_png
#
#     while "there are screenshots":
#         img = queue.get()
#         if img is None:
#             break
#
#         to_png(img.rgb, img.size, output=output.format(number))
#         number += 1
#
#
# if __name__ == "__main__":
#     # The screenshots queue
#     queue = Queue()  # type: Queue
#
#     start = time.time()
#     # 2 processes: one for grabing and one for saving PNG files
#     Process(target=grab, args=(queue,)).start()
#     Process(target=save, args=(queue,)).start()
#     im = Image.frombytes("RGB", queue.get().size, queue.get().bgra, "raw", "BGRX")
#     # im.show()
#
#     end = time.time()
#     print(end - start)