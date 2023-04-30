############################################ 메뉴얼 방식 ############################################
per_origin_prompt = ['[x]는 [MASK]국적을 가진 구성원이다.', '[x]는 [MASK] 국적을 가진 국민이다.', '[x]는 [MASK] 국적을 가진다.'] #실험 가능 데이터
# 0.25040518638573744 0.2633711507293355 0.23612334801762114 -> soft voting : 0.24635332252836303

org_place_of_headquarters_prompt = ['[x]는 [MASK]에 본사가 있다.', '[x]는 [MASK]에 위치한다.', '[x]의 본사가 있는 곳은 [MASK]이다.'] # 실험 가능 데이터
# 0.18598130841121496 0.1411214953271028 0.15481171548117154 -> soft voting : 0.17850467289719626
org_alternate_names_prompt = ['[x]는 [MASK]라고도 불린다.', '[x]는 [MASK]라고 불린다.', '[x]는 [MASK]라는 다른 명칭이 있다.'] # 실험 가능 데이터
# 0.1765151515151515 0.1787878787878788 0.18333333333333332 

############################################ paraphrasing ############################################ 7번 일본어 (어순이 같기 때문에)
per_origin_prompt_paraphraing = ['[x]는 [MASK] 국적을 가진 구성원이다.', '[x]는 [MASK]국적을 가진 국민이다.','[x]은 [MASK] 국적을 가지다.','[MASK]에 국적을 가지고 있는 사람은 [x]이다.']
# (0.25040518638573744 0.2633711507293355 0.23419773095623986), 0.1426256077795786 -> hard voting 3 : 0.24716369529983792
org_place_of_headquarters_prompt_paraphraing = ['[x]는 [MASK]에 본사가 있다.','[x]는 [MASK]에 위치한다.','[x]의 본사가 있는 곳은 [MASK]이다.','MASK에 본사를 둔 회사는 [x]이다.']
# (0.18598130841121496 0.1411214953271028 0.15481171548117154), 0.1589958158995816 -> hard voting 3 : 0.18242677824267783
org_alternate_names_prompt_paraphraing = ['[x]는 [MASK]라고도 불린다.','[x]는 [MASK]로 불린다.','[x]는 [MASK]라는 다른 명칭이 있다.','[x]의 비슷한 이름은 「MASK」이다.']
# (0.1765151515151515 0.17424242424242425 0.18333333333333332), 0.15227272727272728 -> hard voting 3 : 0.1803030303030303

############################################ mining ############################################
per_origin_prompt_mining = ['[x]의 국적은 [MASK] 입니다.','[x]의 국적은 [MASK] 이다.','[x]의 국가는 [MASK] 이다.','[x]는 [MASK] 국적을 가진 국민이다.','[MASK]에 국적을 가진 사람은 [x]이다.']
# (0.2252836304700162 0.22123176661264182 0.2633711507293355), 0.16612641815235007 -> hard voting 3 : 0.22852512155591573
org_place_of_headquarters_prompt_mining = ['[x]는 [MASK]에 본사를 둔 회사이다.','[x]는 [MASK]에 본부의 소재지를 두고 있다.','[x]는 [MASK]에 위치한다.','[MASK]에 본사를 둔 회사는 [x]이다.']
# (0.20920502092050208 0.14811715481171547 0.14058577405857742), 0.1589958158995816 -> hard voting 3 : 0.20418410041841004
org_alternate_names_prompt_mining = ['[x]의 다른 이름은 [MASK]이다', '[x]는 [MASK]로 불려진다.','[x]는 [MASK]라는 비슷한 이름이 있다.','[x]의 비슷한 이름은 [MASK]이다']
# (0.14924242424242423 0.1712121212121212 0.17575757575757575), 0.15227272727272728 -> hard voting 3 : 0.1803030303030303 

############################################ mining + manual(1) = 5 ############################################
per_origin_prompt_mining_manual = ['[x]의 국적은 [MASK] 입니다.','[x]의 국적은 [MASK] 이다.','[x]의 국가는 [MASK] 이다.','[x]는 [MASK] 국적을 가진 국민이다.','[MASK]에 국적을 가진 사람은 [x]이다.','[x]는 [MASK] 국적을 가진 국민이다.']
# 0.22690437601296595 
org_place_of_headquarters_prompt_mining_manual = ['[x]는 [MASK]에 본사를 둔 회사이다.','[x]는 [MASK]에 본부의 소재지를 두고 있다.','[x]는 [MASK]에 위치한다.','[MASK]에 본사를 둔 회사는 [x]이다.', '[x]는 [MASK]에 본사가 있다.']
# 0.198326359832636
org_alternate_names_prompt_mining_manual = ['[x]의 다른 이름은 [MASK]이다', '[x]는 [MASK]로 불려진다.','[x]는 [MASK]라는 비슷한 이름이 있다.','[x]의 비슷한 이름은 [MASK]이다','[x]는 [MASK]라고 불린다.']
# 0.1765151515151515
############################################ paraphrasing + manual(1) = 5 ############################################
per_origin_prompt_paraphraing_manual = ['[x]는 [MASK] 국적을 가진 구성원이다.', '[x]는 [MASK]국적을 가진 국민이다.','[x]은 [MASK] 국적을 가지다.','[MASK]에 국적을 가지고 있는 사람은 [x]이다.','[x]는 [MASK] 국적을 가진 국민이다.']
# 0.23500810372771475
org_place_of_headquarters_prompt_paraphraing_manual = ['[x]는 [MASK]에 본사가 있다.','[x]는 [MASK]에 위치한다.','[x]의 본사가 있는 곳은 [MASK]이다.','[MASK]에 본사를 둔 회사는 [x]이다.','[x]는 [MASK]에 본사가 있다.']
# 0.18410041841004185
org_alternate_names_prompt_paraphraing_manual = ['[x]는 [MASK]라고도 불린다.','[x]는 [MASK]로 불린다.','[x]는 [MASK]라는 다른 명칭이 있다.','[x]의 비슷한 이름은 [MASK]이다.','[x]는 [MASK]라고 불린다.']
# 0.18106060606060606