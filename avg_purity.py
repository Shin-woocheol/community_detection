import pandas as pd


def calculate_average_purity(file_path):
    # 파일을 읽어 들여 데이터프레임으로 변환
    df = pd.read_csv(file_path, delimiter='\t', header=None)

    # purity 컬럼 (여기서는 두 번째 컬럼)의 평균 계산
    average_purity = df[1].mean()

    return average_purity


# 사용 예시
file_path = './output/seed/TC1-6_seed_purity.txt'
average_purity = calculate_average_purity(file_path)
print(f"Average Purity: {average_purity:.4f}")
