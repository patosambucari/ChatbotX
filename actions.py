class ActionBrindarPrecio(Action):
    def name(self) -> Text:
        return "ActionBrindarPrecio"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        if tracker.get_slot("cliente_validado"):
            dispatcher.utter_message("El precio es $100.")
        else:
            dispatcher.utter_message("Para brindarte el precio, necesitamos que ingreses tu número de cuenta.")
        return []
class ActionSolicitarNroCta(Action):
    def name(self) -> Text:
        return "ActionSolicitarNroCta"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message("Por favor, ingresa tu número de cuenta.")
        return []

class ActionValidarNroCta(Action):
    def name(self) -> Text:
        return "ActionValidarNroCta"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        nro_cta = next(tracker.get_latest_entity_values("nro_cta_cliente"), None)

        if re.match(domain['regex']['nro_cta_cliente'], nro_cta):
            dispatcher.utter_message("¡Registrado!")
            return [SlotSet("nro_cta_cliente", nro_cta)]
        else:
            dispatcher.utter_message("Tu cuenta es un número de 5 cifras, que inicia con 5. Verificalo, por favor")
            return []
