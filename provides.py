from charmhelpers.core import hookenv
from charms.reactive import hook
from charms.reactive import RelationBase
from charms.reactive import scopes


class ProvidesElasticsearchStats(RelationBase):
    scope = scopes.GLOBAL

    @hook('{provides:elasticsearch-stats}-relation-{joined,changed}')
    def changed(self):
        self.set_state('{relation_name}.connected')

    @hook('{provides:elasticsearch-stats}-relation-{broken,departed}')
    def broken(self):
        self.remove_state('{relation_name}.connected')

    def configure(self, port):
        relation_info = {
            'host': hookenv.unit_get('private-address'),
            'port': port,
        }

        self.set_remote(**relation_info)
        self.set_state('{relation_name}.configured')
