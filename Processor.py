from strategy.CreateStrategyFile import CreateStrategyFile

class Processor():
    strategy: CreateStrategyFile
    
    def __init__(self, config: dict):
        # Crear la strategia
        self.strategy = CreateStrategyFile.create(config)

        try:
            print("Leyendo el documento...")
            content = self.strategy.reader.read(config)
            print("Cortando el contenido...")
            paragraphs = self.strategy.splitter.split_content(content, config)
            print("Formateando el contenido...")
            formated_content = self.strategy.formatter.format(paragraphs, config)
            # Exportar el resultado
            print("Exportando el resultado...")
            self.strategy.exporter.export(formated_content, config)
            print("---Se ha processado el documento correctamente---")
        except Exception as e:
            print("!!",e)
            