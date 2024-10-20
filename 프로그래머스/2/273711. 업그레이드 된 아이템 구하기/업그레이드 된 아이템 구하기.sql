SELECT A.ITEM_ID, A.ITEM_NAME, A.RARITY 
FROM ITEM_INFO A,
(SELECT D.ITEM_ID 
 FROM ITEM_INFO B, ITEM_TREE C, ITEM_TREE D -- 업그레이드인 아이템 ID만 추출
 WHERE B.ITEM_ID = C.ITEM_ID 
 AND C.ITEM_ID = D.PARENT_ITEM_ID -- C의 ITEM_ID와 D의 PARENT_ITEM_ID 조인
 AND B.RARITY ='RARE' -- 조건은 RARE
) E
WHERE A.ITEM_ID = E.ITEM_ID
ORDER BY A.ITEM_ID DESC