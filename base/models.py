from django.db import models


class BaseModel(models.Model):
    id = models.AutoField(primary_key=True)
    estado = models.BooleanField(default=True)
    created = models.DateField(auto_now=False, auto_now_add=True)
    modified = models.DateField(auto_now=True, auto_now_add=False)
    deleted = models.DateField(auto_now=True, auto_now_add=False)

    class Meta:
        abstract = True


class Category(BaseModel):
    name = models.CharField(max_length=50, null=False, blank=False)

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categorys"

    def __str__(self):
        return self.name


class Author(BaseModel):
    name = models.CharField(max_length=70, null=False, blank=False)
    lastname = models.CharField(max_length=100)
    email = models.EmailField(max_length=200)
    description = models.TextField(blank=True, null=True)

    class Meta:
        verbose_name = "Author"
        verbose_name_plural = "Authors"

    def __str__(self):
        return "{0},{1}".format(self.lastname, self.name)


class Post(BaseModel):
    title = models.CharField(max_length=128, unique=True)
    description = models.TextField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    pub = models.BooleanField("Publicado/No Publicado", default=False)
    date_pub = models.DateField()

    class Meta:
        verbose_name = "Post"
        verbose_name_plural = "Posts"

    def __str__(self):
        return self.title


class Web(BaseModel):
    phone = models.CharField(max_length=10)
    email = models.EmailField(max_length=200)
    adress = models.CharField(max_length=90)

    class Meta:
        verbose_name = "Web"
        verbose_name_plural = "Webs"

    def __str__(self):
        return self.email


class ContactUs(BaseModel):
    name = models.CharField(max_length=120)
    email = models.EmailField(max_length=129)
    asunt = models.TextField()
    message = models.TextField()

    class Meta:
        verbose_name = "Contact"
        verbose_name_plural = "Contacts"

    def __str__(self):
        return self.name


class Suscriptor(BaseModel):
    correo = models.EmailField("Correo Electrónico", max_length=200)

    class Meta:
        verbose_name = "Suscriptor"
        verbose_name_plural = "Suscriptores"

    def __str__(self):
        return self.correo
