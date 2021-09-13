# -*- coding: utf-8 -*-
from django.urls import reverse
from django.db import models
from django.contrib.auth.models import (AbstractBaseUser, BaseUserManager, PermissionsMixin)


class PersonalizadorBaseUserManager(BaseUserManager):
    def create_user(self, usuario, password):
        user = self.model(usuario=usuario)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, usuario, password):
        user = self.create_user(usuario, password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class Usuario(AbstractBaseUser, PermissionsMixin):

    usuario = models.CharField(max_length=100, unique=True, verbose_name='Usuario')
    nome = models.CharField(max_length=100, blank=True, null=True)
    is_active = models.BooleanField(default=True, blank=True, null=True,
                                    verbose_name='Torna Usuario Ativo')
    is_staff = models.BooleanField(default=True, blank=True, null=True,
                                   verbose_name='Torna Usuario Administrador')
    email = models.EmailField(max_length=100, blank=True, null=True)

    USERNAME_FIELD = 'usuario'

    objects = PersonalizadorBaseUserManager()

    def get_full_name(self):
        return self.usuario

    def get_short_name(self):
        return self.usuario



