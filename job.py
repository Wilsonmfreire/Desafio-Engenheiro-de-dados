from pyspark.sql import SparkSession
from pyspark.sql.types import *
from pyspark.sql.functions import *
import pyspark.sql.functions as func

def ganho_total(transacao, contrato):
    desafio = contrato.join(Transacoes, contrato.client_id == Transacoes.client_id, 'left')\
        .filter(contrato.is_active == True)\
        .select(func.round(sum((col('total_amount')-(col('total_amount')*coalesce(col('discount_percentage'),lit(0.0))/100))*col('percentage'))/100,2).alias('mes')\
        .alias('Fechamento'))
        
    return desafio
    
def __main__():

    spark = SparkSession.builder.getOrCreate()

    tTransacao = spark.read.parquet('/Users/wilso/Documents/Desafio/transacoes.parquet')
    tContrato = spark.read.parquet('/Users/wilso/Documents/Desafio/contrato.parquet')

    desafio = ganho_total(tTransacao, tContrato)

    print(desafio.collect())
