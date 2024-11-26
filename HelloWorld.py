import os
import subprocess
from datetime import datetime, timedelta

# 설정: 시작 날짜와 끝 날짜
start_date = datetime(2022, 8, 8)  # 원하는 시작 날짜
end_date = datetime(2024, 11, 25)  # 원하는 끝 날짜

# 설정: 리포지토리 경로
repo_path = os.getcwd()

# 리포지토리로 이동
os.chdir(repo_path)

# 커밋 생성 루프
current_date = start_date
while current_date <= end_date:
    # 날짜 설정
    commit_date = current_date.strftime("%Y-%m-%dT12:00:00")  # 날짜 포맷

    # 파일 수정
    with open("DailyStudy.txt", "a") as file:
        file.write(f"Commit on {current_date}\n")

    # Git 명령 실행
    subprocess.run(["git", "add", "DailyStudy.txt"])
    subprocess.run(
        ["git", "commit", "--date", commit_date, "-m", f"Commit on {current_date}"]
    )

    # 다음 날짜로 이동
    current_date += timedelta(days=1)

# 완료 후 로그 확인
subprocess.run(["git", "log", "--pretty=oneline"])
