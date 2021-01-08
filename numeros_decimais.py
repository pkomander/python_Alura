#interpolação e formatação de numeros

print("R$ {:}".format(1.59))
print("R$ {:f}".format(1.59))#aplicando a formatação com numeros float
print("R$ {:.2f}".format(1.59))#aplicando a formatação monetaria
print("R$ {:.2f}".format(1234.5))
print("R$ {:7.2f}".format(1234.5))#para colocar o ponto decimal alinhados na mesma linha vertical
print("R$ {:07.2f}".format(1.50))#para adicionar zeros antes dos numeros

print("DATA {:2d} /{:2d} ".format(9,4))#O d e utilizando para numeros inteiros
print("DATA {:02d} /{:02d} ".format(9,4))