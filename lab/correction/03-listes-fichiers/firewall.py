# Ecrivez un script qui censure toute lignes contenant liberte ("freedom") dans
# un fichier et qui ecrit le resultat dans un autre fichier

in_file = 'data_in.txt'
out_file = 'data_out.txt'

censor = "THIS LINE HAS BEEN SENSORED BY RAO! LIVE LONG AND UNFREE!\n"

lines = None
with open('data_in.txt', 'r') as fd:
    lines = fd.readlines()
    lines = [line if line.lower().find('freedom') == -1 else censor for line in lines]

with open('data_out.txt', 'w') as fd:
    fd.writelines(lines)
