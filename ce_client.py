from ce_tasks import add
result = add.delay(1, 2)

print(result.ready())
print(result.get(timeout=2))
