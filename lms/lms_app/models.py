from django.db import models

# Create your models here.
class Professor(models.Model):
    def __str__(self):
        return "Nome: " + self.nome + " - Email: " + self.email + " - Login: " + self.login

    nome = models.TextField(max_length=255)
    email = models.TextField(max_length=255)
    celular = models.TextField(max_length=20)
    login = models.TextField(max_length=20)
    senha = models.TextField(max_length=20)

    def save(self):
        print('estou salvando!')
        if(self.login == ''):
            raise Exception('Professor sem login')
        if(self.email == ''):
            self.email = "email nao fornecido"
        professores_login = Professor.objects.filter(login=self.login)
        if len(professores_login) > 0:
            raise Exception ("Login já utilizado")
        super(Professor,self).save()


class Disciplina(models.Model):
    def __str__(self):
        return "Nome: " + self.nome + " - Ementa: " + self.ementa

    nome = models.TextField(max_length=50)
    ementa = models.TextField(max_length=5000)

    def save(self):
        print("estou salvando!")
        disciplina_igual = Disciplina.objects.filter(nome=self.nome)
        if len(disciplina_igual) > 0:
            raise Exception ("Nome da Disciplina já existente")
        super(Disciplina,self).save()


class DisciplinaOfertada(models.Model):
    def __str__(self):
        return "Curso: " + self.curso + " - Turma: " + self.turma + " - Ano: " + self.ano + " - Semestre: " + self.semestre + " - Professor: " + self.professor + " - Disciplina: " + self.disciplina 

    curso = models.TextField(max_length=255)
    turma = models.TextField(max_length=5)
    ano = models.IntegerField() #um inteiro, representa um ano
    semestre = models.IntegerField() #um inteiro, 1 para primeiro sem e 2 para segundo
    professor = models.IntegerField() #id de um professor valido
    disciplina = models.IntegerField() #id de uma disciplina valida

    def save(self):
        print("estou salvando!")
        if (self.curso != "ADS") and (self.curso != "SI") and (self.curso != "BD"):
            raise Exception ("Nome de Curso Inválido")
        curso_igual = DisciplinaOfertada.objects.filter(curso=self.curso)
        ano_igual = DisciplinaOfertada.objects.filter(ano=self.ano)
        turma_igual = DisciplinaOfertada.objects.filter(turma=self.turma)
        semestre_igual = DisciplinaOfertada.objects.filter(semestre=self.semestre)
        disciplina_igual = DisciplinaOfertada.objects.filter(disciplina=self.disciplina)         
        professor_a = DisciplinaOfertada.objects.filter(professor=self.professor) 

        if (len(curso_igual) > 0) and (len(ano_igual) > 0) and (len(turma_igual) > 0) and (len(semestre_igual) > 0) and (len(disciplina_igual) > 0):
            raise Exception ("Disciplinas Repetidas") 
 
        super(DisciplinaOfertada,self).save()

