# Elasticsearch-stats Interface

 This is a Juju charm interface layer. This interface is used to get information
 out of ElasticSearch.

### Examples

#### Requires

If your charm needs to connect to ElasticSearch:

  `metadata.yaml`

```yaml
requires:
  elasticsearch:
    interface: elasticsearch-stats
```

  `layer.yaml`

```yaml
includes: ['interface:elasticsearch-stats']
```  

#### Provides

If your charm needs to provide Elasticsearch connection details:

 `metadata.yaml`

 ```yaml
 provides:
   elasticsearch:
     interface: elasticsearch-stats
 ```

 `layer.yaml`

```yaml
includes: ['interface:elasticsearch-stats']
```  
