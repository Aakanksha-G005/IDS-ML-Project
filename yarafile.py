import yara

rules = yara.compile(filepath='rule.yar')
matches = rules.match('test.txt')

if matches:
    print("🚨 Threat Detected!")
else:
    print("✅ Safe File")