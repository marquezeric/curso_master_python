import clases

persona = clases.Persona()
persona.setNombre("Juan")
persona.setApellidos("Rivera")
persona.setAltura("1.70 cm")
persona.setEdad("45 años")

print(f"La persona es: {persona.getNombre()} {persona.getApellidos()}")
print(persona.hablar())

print("----------------------------------------------------------------")

informatico = clases.Informatico()
informatico.setNombre("Eric")
informatico.setApellidos("Márquez")
informatico.setAltura("1.67 cm")
informatico.setEdad("60 años")

print(f"El informático es: {informatico.getNombre()} {informatico.getApellidos()}")
print(informatico.getLenguajes())
print(informatico.hablar())
print(informatico.caminar())
print(informatico.experiencia)

print("--------------------------------")

tecnico = clases.TecnicoRedes()
tecnico.setNombre("Elmer")
print(tecnico.auditarRedes, tecnico.getNombre(), tecnico.getLenguajes())