import subprocess

# Navn på notebook (må gerne ændres)
notebook = "test.ipynb"

# Placering af notebook (må gerne ændres)
notebook_location = "notebooks/" + notebook

# Placering af pdf (bør ikke ændres)
tex = "pdf/" + notebook.replace(".ipynb", ".tex")

# Nu starter konverteringen
p = subprocess.Popen('echo "Konverterer til pdf..."', shell=True)
p.wait()

# Vi konverterer først notebook til latex
p = subprocess.Popen(
    'jupyter nbconvert --to latex --output-dir=pdf '
    + notebook_location, shell=True)
p.wait()


# Vi tilføjer pakker til latex dokumentet (efter \documentclass{article})
p = subprocess.Popen('echo "Tilføjer pakker..."', shell=True)
p.wait()
with open(tex, 'r') as file:
    data = file.readlines()
data.insert(2, r"\usepackage{braket}")

# Vi skriver ændringerne tilbage til dokumentet
with open(tex, 'w') as file:
    file.writelines(data)

# Nu konverterer vi latex dokumentet til pdf
p = subprocess.Popen('echo "Konverterer til pdf..."', shell=True)
p.wait()
p = subprocess.Popen(
    'pdflatex -output-directory=pdf ' + tex, shell=True)
p.wait()

# Til sidst fjerner vi hjælpefiler
subprocess.Popen('echo "Fjerner diverse filer..."', shell=True)
subprocess.Popen('rm ' + tex, shell=True)
subprocess.Popen('rm pdf/*.aux', shell=True)
subprocess.Popen('rm pdf/*.log', shell=True)
subprocess.Popen('rm pdf/*.out', shell=True)
subprocess.Popen('echo "Konvertering færdig."', shell=True)

# Programmet afsluttes
exit()
