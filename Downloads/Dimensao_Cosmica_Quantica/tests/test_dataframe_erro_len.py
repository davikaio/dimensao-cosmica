; --- Configurações do Expert Advisor Ciborna para PETR4F (M5) ---

Period=5
InpSymbol=PETR4F

; --- Parâmetros de Stop Loss (SL) e Take Profit (TP) ---
; ATENÇÃO: O código MQL5 do EA 'Ciborna' fornecido não possui inputs diretos para SL e TP.
; Estes valores são apenas para referência no arquivo .set e o EA precisaria ser modificado
; para utilizá-los. O gerenciamento de SL/TP seria feito pelo próprio EA se implementado.
StopLossPoints=0.50 ; 50 centavos de loss
TakeProfitPoints=0.30 ; 30 centavos de gain

; --- Parâmetros de Lote ---
; ATENÇÃO: O código MQL5 do EA 'Ciborna' fornecido calcula o volume dinamicamente.
; Se você deseja um lote fixo de 100, o EA precisaria ser modificado para aceitar um input de lote fixo.
LotSize=100

; --- Outros parâmetros do EA Ciborna (conforme código) ---
ADX_Period=14
SAR_Step=0.02
SAR_Maximum=0.2
EMA_Period=20
Volume_Acima_Medio=3.0
Volume_Abaixo_Medio=2.0
Deviation=10
OrderFillingType=ORDER_FILLING_IOC
MagicNumber=0
OrderComment=
StartTime=
EndTime=
TradeMonday=true
TradeTuesday=true
TradeWednesday=true
TradeThursday=true
TradeFriday=true
MaxOpenOrders=1
UseTrailingStop=false
TrailingStopPips=0
UseBreakeven=false
BreakevenPips=0
