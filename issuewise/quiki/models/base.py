import json

from django.db import models
from django.conf import settings
from django.utils.translation import ugettext_lazy as _

from core.utils import last_modified_mixin_factory
from issuewise.utils import get_model_from_settings

LastModifiedMixinClass = last_modified_mixin_factory(version_label = 'latest')


class BaseQuiki(LastModifiedMixinClass):

    _latest_version = models.TextField(_('latest version nobit sequence'))
    latest_internal_version_number = models.IntegerField(_('latest'
        'internal version number'))
    latest_external_version_number = models.IntegerField(_('latest'
        'external version number'))

    @property
    def latest_version(self):
         return json.loads(self._latest_version)
    
    @latest_version.setter
    def latest_version(self, sequence):
        self._latest_version = json.dumps(sequence)

    def get_version(self, version_number):
        
        if version_number == 'latest':
            version_array = self.latest_version

        elif version_number == self.latest_external_version_number:
            version_array = self.latest_version

        else:
            version_dict = self.get_version_dict(version_number)
            version_array = version_dict_to_array(version_dict)

        return version_array

    def get_version_dict(self, version_number):

        edge_operations_model = get_model_from_settings(settings.EDGE_OPERATIONS_MODEL)
        operations = edge_operations_model.objects.get(quiki=self)
        operations = operations.filter(internal_version_number__lte = version_number)
        operations = operations.order_by('internal_version_number')
        version_dict = {}

        for each in operations:
            try:
                del version_dict[each.delete_first_parent]
                del version_dict[each.delete_second_parent]
            except KeyError:
                pass

            if each.add_first_parent:
                version_dict[each.add_first_parent] = each.add_first_child
            if each.add_second_parent:
                version_dict[each.add_second_parent] = each.add_second_child

        return version_dict

    @classmethod
    def version_dict_to_array(version_dict):

        version_array = [-1,]
        next = -1       
        while next != 0:
            next = version_dict[next]
            version_array.append(next)
            
        return version_array

    def add_nobit(self, nobit, external_version_number):
        nobit.save()
        self.latest_internal_version_number += 1
        if nobit.replaced:
            replaced_nobit = nobit.replaced
            delete_first_child = replaced_nobit
            delete_first_parent = replaced_nobit.parent
            delete_second_parent = first_delete_child
            delete_second_child = replaced_nobit.get_child()
            add_first_parent = delete_first_parent
            add_first_child = nobit
            add_second_parent = nobit
            add_second_child = delete_second_child
            change_parent_of_nobit = delete_second_child
            
            replaced_nobit.parent = None
            replaced_nobit.save() # do we need this step?
            
        else:
            delete_first_parent = nobit.parent
            delete_first_child = delete_first_parent.get_child()
            delete_second_parent = None
            delete_second_child = None
            add_first_parent = delete_first_parent
            add_first_child = nobit
            add_second_parent = nobit
            add_second_child = add_first_child
            change_parent_of_nobit = delete_first_child
        
        change_parent_of_nobit.parent = nobit
        change_parent_of_nobit.save() # do we need this step?
        
        edge_operations_model = get_model_from_settings(settings.EDGE_OPERATIONS_MODEL)
        new_operation = edge_operations_model(quiki = self,
            internal_version_number = self.latest_internal_version_number, 
            external_version_number = external_version_number,
            delete_first_parent = delete_first_parent.pk
            delete_first_child = delete_first_child.pk
            delete_second_parent = delete_second_parent.pk
            delete_second_child = delete_second_child.pk
            add_first_parent = add_first_parent.pk
            add_first_child = add_first_child.pk
            add_second_parent = add_second_parent.pk
            add_second_child = add_second_child.pk)
        new_operation.save()
        

            

    class Meta:
        abstract = True
        app_label = 'quiki'


class BaseNobit(models.Model):

    quiki = models.ForeignKey(settings.QUIKI_MODEL,
        related_name = 'nobit_set', verbose_name = _('belongs to quiki'))
    parent = models.ForeignKey('self', null = True, related_name = 'child',
        verbose_name = _('previous nobit in latest version'))
    replaced = models.ForeignKey('self', null = True, 
        related_name = 'replaced_by', verbose_name = _('replaced nobit'))
    special = models.BooleanField(_('special nobit?'), default = True)
    special_value = models.IntegerField(_('type of special nobit'),
        null = True)
        
    # maybe these attributes should go to quiki.py (or the final models) rather
    # than the base?
    theme = models.CharField(_('theme of the text'), max_length = 100)
    
        
    # write the get_child() method and the get_latest_version() manager method
    
    
    

    class Meta:
        abstract = True
        app_label = 'quiki'
        
        
        
class BaseNobitManager(models.Manager):

    get_child

    


class BaseEdgeOperation(models.Model):

    # the edge operations table is used to systematically generate the versions
    # corresponding to a particular Quiki

    quiki = models.ForeignKey(settings.QUIKI_MODEL,
        related_name = 'edge_operations_set', 
        verbose_name = _('edge operation of quiki'))
    
    internal_version_no = models.IntegerField(_('internal version number'))

    external_version_no = models.IntegerField(_('external version number'))

    add_first_parent = models.IntegerField(_('parent in first added edge'),
        null = True)

    add_first_child = models.IntegerField(_('child in first added edge'),
        null = True)

    add_second_parent = models.IntegerField(_('parent in second added edge'),
        null = True)

    add_second_child = models.IntegerField(_('child in second added edge'),
        null = True)

    delete_first_parent = models.IntegerField(_('parent in first deleted edge'),
        null = True)

    delete_first_child = models.IntegerField(_('child in first deleted edge'),
        null = True)

    delete_second_parent = models.IntegerField(_('parent in second deleted edge'),
        null = True)

    delete_second_child = models.IntegerField(_('child in seconde deleted edge'),
        null = True)

    
    class Meta:
        abstract = True
        app_label = 'quiki'
    

    

    
        

    

    

    
    
   
    
    
    

    