from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
# Create your models here.

GEMDER_TYPE = (
    ('M', 'Male'),
    ('F', 'Female'),
)

class MemberType(models.Model):
    """Model definition for MemberType.
    Using this as to identify Sewadar, IC, and Admin"""

    name = models.CharField(max_length=50)
    description = models.TextField(blank=True)

    class Meta:
        """Meta definition for MemberType."""

        verbose_name = 'MemberType'
        verbose_name_plural = 'MemberTypes'

    def __str__(self):
        """Unicode representation of MemberType."""
        return self.name

    # def save(self):
    #     """Save method for MemberType."""
    #     pass

    # def get_absolute_url(self):
    #     """Return absolute url for MemberType."""
    #     return ('')

    # TODO: Define custom methods here

class MemberList(models.Model):
    """Model definition for MemberList."""

    # ID and FK
    MemberTypeDetails = models.ForeignKey('webui.MemberType', on_delete=models.DO_NOTHING)
    CenterDetails = models.ForeignKey('webui.Center', on_delete=models.DO_NOTHING)
    id = models.BigIntegerField(unique=True,primary_key=True)

    name = models.CharField(max_length=50)
    father_name = models.CharField(max_length=50,blank=True)
    # Can make a relation
    gender = models.CharField(choices=GEMDER_TYPE,default='M', max_length=10)
    contact = PhoneNumberField()
    altcontact = PhoneNumberField(blank=True)
    department = models.CharField(max_length=50, default="Security")

    class Meta:
        """Meta definition for MemberList."""

        verbose_name = 'MemberList'
        verbose_name_plural = 'MemberLists'

    def __str__(self):
        """Unicode representation of MemberList."""
        return '{}'.format(self.name ) # TODO

    # def save(self):
    #     """Save method for MemberList."""
    #     pass

    # def get_absolute_url(self):
    #     """Return absolute url for MemberList."""
    #     return ('')

    # TODO: Define custom methods here

class Center(models.Model):
    """Model definition for Center."""

    name = models.CharField(max_length=50)

    class Meta:
        """Meta definition for Center."""

        verbose_name = 'Center'
        verbose_name_plural = 'Centers'

    def __str__(self):
        """Unicode representation of Center."""
        return '{}'.format(self.name ) # TODO

    # def save(self):
    #     """Save method for Center."""
    #     pass

    # def get_absolute_url(self):
    #     """Return absolute url for Center."""
    #     return ('')

    # TODO: Define custom methods here

class SecurityPost(models.Model):
    """Model definition for SecurityPost."""

    name = models.CharField(max_length=50)


    class Meta:
        """Meta definition for SecurityPost."""

        verbose_name = 'SecurityPost'
        verbose_name_plural = 'SecurityPosts'

    def __str__(self):
        """Unicode representation of SecurityPost."""
        return '{}'.format(self.name ) # TODO

    def save(self):
        """Save method for SecurityPost."""
        pass

    def get_absolute_url(self):
        """Return absolute url for SecurityPost."""
        return ('')

    # TODO: Define custom methods here

class Transaction(models.Model):
    """Model definition for Transaction."""

    MemberDetails = models.ForeignKey('webui.MemberList', on_delete=models.DO_NOTHING)
    inTime = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        """Meta definition for Transaction."""

        verbose_name = 'Transaction'
        verbose_name_plural = 'Transactions'

    def __str__(self):
        """Unicode representation of Transaction."""
        return '{}'.format(self.inTime ) # TODO

    # def save(self):
    #     """Save method for Transaction."""
    #     pass

    # def get_absolute_url(self):
    #     """Return absolute url for Transaction."""
    #     return ('')

    # TODO: Define custom methods here





# OPen Transdaction 

class MemberListOpen(models.Model):
    """Model definition for MemberListOpen."""

    # ID and FK
    CenterDetails = models.ForeignKey('webui.Center', on_delete=models.DO_NOTHING)

    MemberTypeDetails = models.CharField(default='Sewadaar', max_length=50)
    name = models.CharField(max_length=50)
    father_name = models.CharField(max_length=50,blank=True)
    # Can make a relation
    gender = models.CharField(choices=GEMDER_TYPE,default='M', max_length=10)
    contact = PhoneNumberField()
    altcontact = PhoneNumberField(blank=True)
    department = models.CharField(max_length=50, default="Security")

    class Meta:
        """Meta definition for MemberListOpen."""

        verbose_name = 'MemberListOpen'
        verbose_name_plural = 'MemberListOpens'

    def __str__(self):
        """Unicode representation of MemberListOpen."""
        return '{}'.format(self.name ) # TODO

    # def save(self):
    #     """Save method for MemberListOpen."""
    #     pass

    # def get_absolute_url(self):
    #     """Return absolute url for MemberListOpen."""
    #     return ('')

    # TODO: Define custom methods here


class TransactionOpen(models.Model):
    """Model definition for TransactionOpen."""

    MemberDetails = models.ForeignKey('webui.MemberListOpen', on_delete=models.DO_NOTHING)
    inTime = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        """Meta definition for TransactionOpen."""

        verbose_name = 'TransactionOpen'
        verbose_name_plural = 'TransactionOpens'

    def __str__(self):
        """Unicode representation of TransactionOpen."""
        return '{}'.format(self.inTime ) # TODO

    # def save(self):
    #     """Save method for TransactionOpen."""
    #     pass

    # def get_absolute_url(self):
    #     """Return absolute url for TransactionOpen."""
    #     return ('')

    # TODO: Define custom methods here

