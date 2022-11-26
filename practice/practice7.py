# 파일 입출력 w: 쓰기(덮어쓰기), a: append 이어쓰기, r: 읽기
score_file = open("score.txt", "w", encoding="utf8")
print("수학: 0", file=score_file)
print("영어: 50", file=score_file)
score_file.close()

score_file = open("score.txt", "a", encoding="utf8")
score_file.write("과학: 80")
score_file.write("\n코딩: 100")
score_file.close()
print("---")
score_file = open("score.txt", "r", encoding="utf8")
print(score_file.read())
score_file.close()
print("---")
# 줄별로 읽기, 한 줄 읽고 커서는 다음 줄로 이동
score_file = open("score.txt", "r", encoding="utf8")
print(score_file.readline(), end="")
print(score_file.readline(), end="")
print(score_file.readline(), end="")
print(score_file.readline())
score_file.close()
print("---")
score_file = open("score.txt", "r", encoding="utf8")
while True:
    line = score_file.readline()
    if not line:
        break
    print(line, end="")
score_file.close()
print()
print("---")
score_file = open("score.txt", "r", encoding="utf8")
lines = score_file.readlines()
for line in lines:
    print(line, end="")
score_file.close()
print()
print("----------------")

# pickle
import pickle
profile_file = open("profile.pickle", "wb") # w: 쓰기, b: binary type => pickle 은 항상 지정해 줘야 함
profile = {"이름": "가가가", "나이": 20, "취미": ["독서", "산책", "코딩"]}
print(profile)
# profile 에 있는 정보를 file 에 저장
pickle.dump(profile, profile_file)
profile_file.close()
print("---")
profile_file = open("profile.pickle", "rb")
# file 에 있는 정보를 profile 에 불러오기
profile_read = pickle.load(profile_file)
print(profile_read)
profile_file.close()

print("----------------")
#with close() 할 필요가 없다
with open("profile.pickle", "rb") as profile_file:
    print(pickle.load(profile_file))

with open("study_python", "w", encoding="utf8") as study_file:
    study_file.write("파이썬 공부 중")
print("---")
with open("study_python", "r", encoding="utf8") as study_file:
    print(study_file.read())














