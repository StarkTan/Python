"""
人脸识别库 face_recognition 使用
"""
import face_recognition
import cv2 as cv

target_img_file = "data/target.jpg"  # 目标人脸
# 加载图片
# file 加载的文件 mode 是加载图片的数据格式
target_image = face_recognition.load_image_file(file=target_img_file, mode='RGB')
# 人脸定位 target_image 图片数据，number_of_times_to_upsample 处理精度(数值越大越耗时) model人脸匹配模式 eg：cnn，hog
# 返回数值 内容[(top, right, bottom, left),(...)]
face_locations = face_recognition.face_locations(target_image, number_of_times_to_upsample=1, model='hog')
# 人脸编码 known_face_locations（可选）已知的人脸位置 num_jitters：处理次数 数值越大耗时越长，返回为所有人脸的编码数组
target_face_encodings = face_recognition.face_encodings(target_image, known_face_locations=face_locations, num_jitters=1)

test_img_file = 'data/test.jpg'
test_image = face_recognition.load_image_file(test_img_file)
face_locations = face_recognition.face_locations(test_image)
face_encodings = face_recognition.face_encodings(test_image, face_locations)

img = cv.imread(target_img_file, flags=cv.IMREAD_UNCHANGED)
cv.imshow(winname='image', mat=img)  # 将图片显示出来,闪退
cv.waitKey(0)  # 0 表示一直等待键盘操作, 触发是可以获取键盘输入值
cv.destroyAllWindows()


img = cv.imread(test_img_file, flags=cv.IMREAD_UNCHANGED)

for face_location, face_encoding in zip(face_locations, face_encodings):
    # 判断是否是同一张人脸。tolerance 判断的阈值 返回布尔值
    # face_distance(face_encodings, face_to_compare) 判断两张人脸的数值的差异
    if face_recognition.compare_faces(target_face_encodings, face_encoding, tolerance=0.6)[0]:
        cv.rectangle(img, (face_location[3], face_location[0]), (face_location[1], face_location[2]), (0, 255, 0), 2)

cv.imshow(winname='image', mat=img)  # 将图片显示出来,闪退
cv.waitKey(0)  # 0 表示一直等待键盘操作, 触发是可以获取键盘输入值
cv.destroyAllWindows()
