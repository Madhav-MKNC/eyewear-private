import boto3
import json
import cv2
import random
import numpy as np

D = {}
Dic = {}
cont = []
for a in range(1,5):
    for b in range(1,3):
        for c in range(1,3):
            for d in range(1,4):
                D[vec(a,b,c,d)]=[]
                Dic[vec(a,b,c,d)]=[]

# def contour(path):
#     img = cv2.imread(path)
#     gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#     edges = cv2.Canny(gray, 100, 200)

#     ret, thresh = cv2.threshold(edges, 127, 255, cv2.THRESH_BINARY)

#     contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    
#     return contours


def cont_compare(a,b):
    # diff = np.abs(a - b)
    # for i in range(len(diff)):
    #     for j in range(len(diff[i])):
    #     # Add the current element to the sum
    #         sum += diff[i][j]
            
    cnt1 = a[0]
    cnt2 = b[0]
    ret = cv2.matchShapes(cnt1,cnt2,1,0.0)
        
    return ret


# total_data = 50
# for i in range (1,total_data+1):
#     s = "C:\Users\mohda\OneDrive\Desktop\Warpspeed\Countours\c"
#     path = s+str(i)+".png"
    
def get_contour(img):

    # img = cv2.imread(path)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    edges = cv2.Canny(gray, 100, 200)
    ret, thresh = cv2.threshold(edges, 127, 255, cv2.THRESH_BINARY)
    contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    
    return contours


def detect_faces(photo, bucket, region):
    
    session = boto3.Session(profile_name='Areeb',
                            region_name=region)
    client = session.client('rekognition', region_name=region)

    response = client.detect_faces(Image={'S3Object':{'Bucket':bucket,'Name':photo}},
                                   Attributes=['ALL'])

    print('Detected faces for ' + photo)
#     for faceDetail in response['FaceDetails']:
#         print('The detected face is between ' + str(faceDetail['AgeRange']['Low'])
#               + ' and ' + str(faceDetail['AgeRange']['High']) + ' years old')

#         print('Here are the other attributes:')
#         print(json.dumps(faceDetail, indent=4, sort_keys=True))

#         Access predictions for individual face details and print them
#         print("Gender: " + str(faceDetail['Gender']))
#         print("Smile: " + str(faceDetail['Smile']))
#         print("Eyeglasses: " + str(faceDetail['Eyeglasses']))
#         print("Face Occluded: " + str(faceDetail['FaceOccluded']))
#         print("Emotions: " + str(faceDetail['Emotions'][0]))
    return  (response['FaceDetails'])

def vec(face_details):
    age_det = (face_details[0]['AgeRange']['Low'] + face_details[0]['AgeRange']['High'])/2
    if(age_det<20): age = 1
    elif(age_det<40): age = 2
    elif(age_det<60): age = 3
    else: age = 4

    if(face_details[0]['Gender']['Value']=="Male"): gender = 1
    else: gender = 2

    if(face_details[0]['Mustache']['Value']): mustache = 1
    else: mustache = 2

    conf = face_details[0]['Beard']['Confidence']
    if(conf>80): beard = 1
    elif(conf>65): beard = 2
    else: beard = 3

    return f"{age}{gender}{mustache}{beard}"


def assign_glasses(L,cont):
    if(len(L)!=0):
        min_idx=0
        cmp_min = 0
        cmp=0
        for k in range(0,7):
            if(cmp_min==0):
                cmp_min=cmp
            if cmp<=cmp_min:
                cmp_min=cmp
                min_idx=k-1
            cmp = 0
            for img_cont in L:
                cmp = cmp + cont_compare(cont[k],img_cont)
        return min_idx
    else:
        return -1
    


def main():
    s = "C:/Users/mohda/OneDrive/Desktop/Warpspeed/Contours/c"
    for i in range(1,8):
        path = s+str(i)+".png"
        I = cv2.imread(path)
        cont.append(get_contour(I))
    
    total_data = 345
    bucket = "warpspeedgenai"
    region = "ap-south-1"
    # loc = "C:/Users/mohda/OneDrive/Desktop/classification/"
    for i in range(1,total_data+1):
        path = str(i)+".jpg"
        path_dat = "C:/Users/mohda/OneDrive/Desktop/classification/"
        path_dat = path_dat+str(i)+".jpg"
        Img = cv2.imread(path_dat)

        face_details = detect_faces(path)
        age_det = (face_details[0]['AgeRange']['Low'] + face_details[0]['AgeRange']['High'])/2
        if(age_det<20): age = 1
        elif(age_det<40): age = 2
        elif(age_det<60): age = 3
        else: age = 4

        if(face_details[0]['Gender']['Value']=="Male"): gender = 1
        else: gender = 2

        if(face_details[0]['Mustache']['Value']): mustache = 1
        else: mustache = 2

        conf = face_details[0]['Beard']['Confidence']
        if(conf>80): beard = 1
        elif(conf>65): beard = 2
        else: beard = 3

        def vec(age,gender,mustache,beard)


        for age in range(1,5):
            for gender in range(1,3):
                for mustache in range(1,3):
                    for beard in range(1,4):
                        (D[vec(age,gender,mustache,beard)]).append(get_contour(Img))

if __name__ == "__main__":
    for a in range(1,5):
        for b in range(1,3):
            for c in range(1,3):
                for d in range(1,4):
                    D[vec(a,b,c,d)]=[]
                    Dic[vec(a,b,c,d)]=[]
    main()
    
    


for a in range(1,5):
    for b in range(1,3):
        for c in range(1,3):
            for d in range(1,4):
                if(assign_glasses(D[vec(a,b,c,d)],cont)!=-1):
                    Dic[vec(a,b,c,d)] = cont[assign_glasses(D[vec(a,b,c,d)],cont)]
                else:
                    Dic[vec(a,b,c,d)] = cont[random.randint(0,6)]
                    
                    

print(len(D))
print(len(Dic))

