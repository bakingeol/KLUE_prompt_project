per_origin_prompt = ['[x]는 [MASK]국적을 가진 구성원이다.', '[x]는 [MASK] 국적을 가진 국민이다.', '[x]는 [MASK] 국적을 가진다.'] #실험 가능 데이터
'''
0.25040518638573744 0.2633711507293355 0.23612334801762114 -> soft voting : 0.24635332252836303
'''
org_place_of_headquarters_prompt = ['[x]는 [MASK]에 본사가 있다.', '[x]는 [MASK]에 위치한다.', '[x]는 [MASK]에 있다.'] # 실험 가능 데이터
# 0.18598130841121496 0.1411214953271028 0.0514018691588785 -> soft voting : 0.17850467289719626
org_alternate_names_prompt = ['[x]는 [MASK]라고도 불린다.', '[x]는 [MASK]라고 불린다.', '[x]는 [MASK]라는 다른 명칭이 있다.'] # 실험 가능 데이터
# 0.18021793797150043 0.18189438390611903 0.18440905280804695 