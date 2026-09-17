from ml_engine import MLEngine

engine = MLEngine()

result = engine.classify_modbus(
    49389,
    52921,
    25770,
    13625
)

print(result)