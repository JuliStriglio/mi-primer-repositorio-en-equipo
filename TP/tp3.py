import cv2
import numpy as np
import os


def generate_marker(marker_id, marker_size, filename):
    # Define el diccionario ArUco
    aruco_dict = cv2.aruco.getPredefinedDictionary(cv2.aruco.DICT_6X6_250)

    # Genera el marcador
    marker_image = cv2.aruco.generateImageMarker(aruco_dict, marker_id, marker_size)

    # Guarda la imagen del marcador
    cv2.imwrite(filename, marker_image)

    # Muestra el marcador
    cv2.imshow('ArUco Marker', marker_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# Generar el marcador si no existe
marker_id = 42
marker_size = 200
marker_filename = 'aruco_marker.png'
if not os.path.exists(marker_filename):
    generate_marker(marker_id, marker_size, marker_filename)

# Define el diccionario ArUco
aruco_dict = cv2.aruco.getPredefinedDictionary(cv2.aruco.DICT_6X6_250)
parameters = cv2.aruco.DetectorParameters()

# Cargar la imagen que queremos superponer
overlay_img = cv2.imread('pokemon.webp')
overlay_img = cv2.resize(overlay_img, (200, 200))  # Ajusta el tamaño según sea necesario

def overlay_on_marker(frame, corners, overlay_img):
    if corners is None:
        return frame

    pts_dst = corners.reshape(4, 2)
    h, w = overlay_img.shape[:2]
    pts_src = np.array([
        [0, 0],
        [w - 1, 0],
        [w - 1, h - 1],
        [0, h - 1]
    ], dtype="float32")

    M = cv2.getPerspectiveTransform(pts_src, pts_dst)
    warped = cv2.warpPerspective(overlay_img, M, (frame.shape[1], frame.shape[0]))

    mask = np.zeros_like(frame, dtype="uint8")
    cv2.fillConvexPoly(mask, np.int32(pts_dst), (255, 255, 255))
    mask = cv2.bitwise_not(mask)
    frame_bg = cv2.bitwise_and(frame, mask)
    frame_fg = cv2.bitwise_and(warped, cv2.bitwise_not(mask))

    result = cv2.add(frame_bg, frame_fg)
    return result

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    corners, ids, _ = cv2.aruco.detectMarkers(gray, aruco_dict, parameters=parameters)

    if ids is not None and marker_id in ids:
        idx = np.where(ids == marker_id)[0][0]
        frame = overlay_on_marker(frame, corners[idx], overlay_img)

    cv2.aruco.drawDetectedMarkers(frame, corners, ids)
    cv2.imshow('AR ArUco Marker', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

