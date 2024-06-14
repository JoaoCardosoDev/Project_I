# Entrega 14-06 - Projecto_I

## *Estrutura de dados*

Desde da última entrega, em termos de backoffice, a grande maioria das funcionalidades estão implementadas, estando satisfeito em termos de backoffice avancei para o front office com o projeto de figma onde completei a landing page:

https://www.figma.com/design/RVWY9VaP7YIpGbPDQdHiYT/Untitled?node-id=0-1&t=rUDHc56UD9pU6jLT-1

Estou agora a fazer os webcomponents.

### Fica aqui o detalhe dos modelos:

Os modelos do projeto estão desenhados em base de inheritance, em que temos um modelo Base:

**Base**
```
    id = models.BigAutoField(primary_key=True)
    date = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=30)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
```
 E a partir deste model tenho mais dois, o de Folder e File:

**Folder**
```
    parent = models.ForeignKey('Folder', on_delete=models.CASCADE, related_name='folder_children', null=True, blank=True)
    
    def __str__(self):
        return f"{self.title}"
```
**File**
```
    parent = models.ForeignKey(Folder, on_delete=models.CASCADE, null=True, blank=True)
    storage = models.FileField()

    def __str__(self):
        return f"{self.title}"
    
    def save(self, *args, **kwargs):
        self.storage.name = f"{self.title}"
        super().save(*args, **kwargs)
```

Os modelos estão com overide do nome da instance no Admin para o title para motivos de debugg. Estão com Foreign keys para estabelecer relações sendo a folder relacionada ao próprio modelo. 

E por fim existe um overide do safe para que o nome do que é uploaded seja igual ao que é inputed no momento de intanciamento. Este workaround resolveu um problema na view de download em que o nome do ficheiro não coincidia com o user input.

# Entrega 06-06 - Projeto_I

## *Estrutura inicial do projeto*

Projeto até ao momento está com os módulos de login e sign in feitos. O sistema de folders e files está WIP e a UI está em suspenso até as funcionalidades básicas estarem acabadas (Minimum viable product).

Docker, Makefile e poetry estão 90% feitos, penso ainda haver alguns pormenores em falta.

Os modelos ainda estão com falhas graves, ainda tenho que perceber bem se é necessário ser explícito com o path.

Os modelos de momento são File e Folder a fazer inherit de uma base com campos em comum.

Vou continuar a trabalhar nos forms, a seguir vou para o UX com botões para apagar editar etc, e depois trabalhar na UI.

https://github.com/JoaoCardosoDev/Project_I/releases/tag/06-06

