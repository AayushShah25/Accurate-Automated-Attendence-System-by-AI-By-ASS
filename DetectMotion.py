import cv2


def Movement(frame1, frame2):

    absDiff = cv2.absdiff(frame1,frame2)
    absDiff = cv2.cvtColor(absDiff, cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(absDiff,(15,15), 0)
    _, thresh = cv2.threshold(blurred,70,255,cv2.THRESH_BINARY)
    dialated = cv2.dilate(thresh,None,iterations = 6)
    contours, hierarchy = cv2.findContours(dialated,cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    for c in contours:
        if cv2.contourArea(c) > 3500:
            return True


    return False








