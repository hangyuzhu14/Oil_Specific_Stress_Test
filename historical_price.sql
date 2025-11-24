SELECT
    CurveKey,
    CurveName,
    TradingDate,
    DeliveryDate,
    MidPrice,
    Currency,
    Unit,
    RelativeDeliveryPeriod
FROM LiD.Business."Team_London_Risk".Oil."Stress Testing"."Prices Final"
WHERE TradingDate <= '{cob}' and TradingDate >= '{cob_5y_str}'

UNION ALL


SELECT 
    CurveKey,
    SPLIT_PART(CurveName, 'GLOBAL', 1) AS CurveName,
    TradingDate,
    CAST(DATE_TRUNC('MONTH', DeliveryDate) AS DATE) AS DeliveryDate,
    Bid AS MidPrice,
    'USD' AS Currency,
    Denominator AS Unit,
    CAST(months_between(DeliveryDate, TradingDate) AS INT) AS RelativeDeliveryPeriod
FROM Core.Preparation.MIX.RAW.EndurRaw.ForwardOutput
WHERE CurveKey = '2hzz0' and TradingDate <= '{cob}' and TradingDate >= '{cob_5y_str}'
