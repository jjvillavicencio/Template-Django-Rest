# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Categoria(models.Model):
    ctgr_id = models.AutoField(primary_key=True)
    ctgr_nombre = models.CharField(max_length=50)
    ctgr_descripcion = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'categoria'


class Compra(models.Model):
    cmpr_id = models.AutoField(primary_key=True)
    cmpr_estado = models.CharField(max_length=50)
    cmpr_valor = models.DecimalField(max_digits=10, decimal_places=0)
    cmpr_observacion = models.TextField(blank=True, null=True)
    cmpr_fecha = models.DateTimeField()
    cmpr_cantidad_productos = models.IntegerField()
    tpgo = models.ForeignKey('TipoPago', models.DO_NOTHING)
    ntgr = models.ForeignKey('Entrega', models.DO_NOTHING)
    usr = models.ForeignKey('Usuario', models.DO_NOTHING)
    sprm = models.ForeignKey('Supermercado', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'compra'


class Entrega(models.Model):
    ntrg_id = models.AutoField(primary_key=True)
    ntgr_nombre = models.CharField(max_length=50)
    ntgr_descripcion = models.TextField()

    class Meta:
        managed = False
        db_table = 'entrega'


class Lista(models.Model):
    lst_id = models.AutoField(primary_key=True)
    lst_nombre = models.CharField(max_length=50)
    lst_color = models.CharField(max_length=10)
    lst_valor_total = models.DecimalField(max_digits=10, decimal_places=0)
    lst_creacion = models.DateTimeField()
    lst_ultima_compra = models.DateTimeField(blank=True, null=True)
    lst_cant_art = models.IntegerField()
    usr = models.ForeignKey('Usuario', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'lista'


class Producto(models.Model):
    prdct_id = models.AutoField(primary_key=True)
    prdct_nombre = models.CharField(max_length=50)
    prdct_imagen = models.CharField(max_length=50)
    prdct_codigo_barras = models.CharField(max_length=50, blank=True, null=True)
    prdct_precio = models.DecimalField(max_digits=10, decimal_places=0)
    prdct_unidad = models.CharField(max_length=10)
    prdct_contenido = models.DecimalField(max_digits=10, decimal_places=0)
    prdct_stock = models.IntegerField()
    scrsl = models.ForeignKey('Sucursal', models.DO_NOTHING)
    ctgr = models.ForeignKey(Categoria, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'producto'


class Sucursal(models.Model):
    scrsl_id = models.AutoField(primary_key=True)
    scrsl_pais = models.CharField(max_length=50)
    scrsl_provincia = models.CharField(max_length=50)
    scrsl_ciudad = models.CharField(max_length=50)
    scrsl_direccion = models.CharField(max_length=50)
    scrsl_coordenadas = models.TextField()  # This field type is a guess.
    sprm = models.ForeignKey('Supermercado', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'sucursal'


class Supermercado(models.Model):
    sprm_id = models.AutoField(primary_key=True)
    sprm_identificacion = models.CharField(max_length=50)
    sprm_nombre = models.CharField(max_length=50)
    sprm_logo = models.CharField(max_length=50)
    sprm_telefono = models.CharField(max_length=10)

    class Meta:
        managed = False
        db_table = 'supermercado'


class TipoPago(models.Model):
    tpgo_id = models.AutoField(primary_key=True)
    tpgo_nombre = models.CharField(max_length=50)
    tpgo_descripcion = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'tipo_pago'


class Usuario(models.Model):
    usr_id = models.AutoField(primary_key=True)
    usr_nombre = models.CharField(max_length=50)
    usr_apellido = models.CharField(max_length=50)
    usr_cedula_identidad = models.CharField(max_length=11)
    usr_facebook = models.CharField(max_length=50)
    usr_fecha_nacimiento = models.DateField()
    usr_avatar = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'usuario'
