# 0. 모듈 로딩
from matplotlib import font_manager,rc


# 함수 기능 : 시각화시 폰트 설정
# 함수 이름: set_Koreantxt
# 매개 변수: font_path
# 반환 값: None

def set_Koreantxt(font_path):
    # 설정할 한글 폰트 이름 추출
    font_name = font_manager.FontProperties(fname=font_path).get_name()
    # 한글 폰트 설정
    rc('font', family=font_name)
    # 확인 출력
    print(f'[폰트 설정] \n{font_name}')

    
