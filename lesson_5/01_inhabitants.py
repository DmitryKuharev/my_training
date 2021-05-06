
# Вывести на консоль жителей комнат (модули room_1 и room_2)
# Формат: В комнате room_1 живут: ...



import room_1
import room_2

print('В комнате {} живут: {}'.format(room_1.__name__, ', '.join(room_1.folks)))
print('В комнате {} живут: {}'.format(room_2.__name__, ', '.join(room_2.folks)))


