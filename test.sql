SELECT 
    CurveKey,
    SPLIT_PART(CurveName, 'GLOBAL', 1) AS CurveName,
    TradingDate,
    CAST(DATE_TRUNC('MONTH', DeliveryDate) AS DATE) AS DeliveryDate,
    CAST(months_between(DeliveryDate, TradingDate) AS INT) AS RelativeDeliveryPeriod,
    Bid AS MidPrice,
    'USD' AS Currency,
    Denominator AS Unit
FROM Core.Preparation.MIX.RAW.EndurRaw.ForwardOutput
WHERE CurveKey = '2hzz0';