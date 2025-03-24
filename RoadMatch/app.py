from flask import Flask, request, render_template, redirect, url_for, session
from Paquete_Filtros.filtros import *
from Paquete_datos.datos_autos import lista_autos 

app = Flask(__name__)
app.secret_key = 'clave_secreta'

@app.route("/")
def menu_principal():
    """
    Muestra el menú principal. Si no hay autos filtrados en la sesión,
    se inicializa con la lista completa de autos.
    """
    if "autos_filtrados" not in session:
        session["autos_filtrados"] = lista_autos
    return render_template("menu_principal.html")

@app.route('/reiniciar')
def reiniciar():
    """
    Reinicia los filtros y restablece la lista completa de autos.
    """
    session["autos_filtrados"] = lista_autos
    return redirect(url_for('menu_principal'))

@app.route('/filtro/marca', methods=['GET'])
def filtro_marca():
    """
    Filtra los autos por marca.
    Si se proporciona una marca, se aplica el filtro y se actualiza la sesión.
    """
    marca = request.args.get('marca')
    base = session.get("autos_filtrados", lista_autos)
    if marca:
        filtro = FiltroMarca(base)
        autos_filtrados = filtro.aplicar(base, marca)
        session["autos_filtrados"] = autos_filtrados
        return redirect(url_for("menu_principal"))
    return render_template("filtro_marca.html")

@app.route('/filtro/año', methods=['GET'])
def filtro_año():
    """
    Filtra los autos por año dentro de un rango determinado.
    """
    min_año = request.args.get('min_año', type=int)
    max_año = request.args.get('max_año', type=int)
    base = session.get("autos_filtrados", lista_autos)
    if min_año is not None and max_año is not None:
        filtro = FiltroAño(base)
        autos_filtrados = filtro.aplicar(base, min_año, max_año)
        session["autos_filtrados"] = autos_filtrados
        return redirect(url_for("menu_principal"))
    return render_template("filtro_año.html")

@app.route('/filtro/presupuesto', methods=['GET'])
def filtro_presupuesto():
    """
    Filtra los autos por presupuesto dentro de un rango determinado.
    """
    min_presupuesto = request.args.get('min_presupuesto', type=float)
    max_presupuesto = request.args.get('max_presupuesto', type=float)
    base = session.get("autos_filtrados", lista_autos)
    if min_presupuesto is not None and max_presupuesto is not None:
        filtro = FiltroPresupuesto(base)
        autos_filtrados = filtro.aplicar(base, min_presupuesto, max_presupuesto)
        session["autos_filtrados"] = autos_filtrados
        return redirect(url_for("menu_principal"))
    return render_template("filtro_presupuesto.html")

@app.route('/filtro/kilometros', methods=['GET'])
def filtro_kilometros():
    """
    Filtra los autos por kilometraje dentro de un rango determinado.
    """
    min_km = request.args.get('min_km', type=int)
    max_km = request.args.get('max_km', type=int)
    base = session.get("autos_filtrados", lista_autos)
    if min_km is not None and max_km is not None:
        filtro = FiltroKilometros(base)
        autos_filtrados = filtro.aplicar(base, min_km, max_km)
        session["autos_filtrados"] = autos_filtrados
        return redirect(url_for("menu_principal"))
    return render_template("filtro_kilometros.html")

@app.route('/filtro/transmision', methods=['GET'])
def filtro_transmision():
    """
    Filtra los autos por tipo de transmisión.
    """
    transmision = request.args.get('transmision')
    base = session.get("autos_filtrados", lista_autos)
    if transmision:
        filtro = FiltroTransmicion(base)
        autos_filtrados = filtro.aplicar(base, transmision)
        session["autos_filtrados"] = autos_filtrados
        return redirect(url_for("menu_principal"))
    return render_template("filtro_transmision.html")

@app.route('/filtro/uso', methods=['GET'])
def filtro_uso():
    """
    Filtra los autos según su uso (nuevo o usado).
    """
    uso = request.args.get('uso')
    base = session.get("autos_filtrados", lista_autos)
    if uso:
        filtro = FiltroUso(base)
        autos_filtrados = filtro.aplicar(base, uso)
        session["autos_filtrados"] = autos_filtrados
        return redirect(url_for("menu_principal"))
    return render_template("filtro_uso.html")

@app.route('/filtro/carroceria', methods=['GET'])
def filtro_carroceria():
    """
    Filtra los autos por tipo de carrocería.
    """
    carroceria = request.args.get('carroceria')
    base = session.get("autos_filtrados", lista_autos)
    if carroceria:
        filtro = FiltroCarroceria(base)
        autos_filtrados = filtro.aplicar(base, carroceria)
        session["autos_filtrados"] = autos_filtrados
        return redirect(url_for("menu_principal"))
    return render_template("filtro_carroceria.html")

@app.route('/filtro/consumo', methods=['GET'])
def filtro_consumo():
    """
    Filtra los autos por consumo de combustible.
    """
    consumo = request.args.get('consumo')
    base = session.get("autos_filtrados", lista_autos)
    if consumo:
        filtro = FiltroConsumo(base)
        autos_filtrados = filtro.aplicar(base, consumo)
        session["autos_filtrados"] = autos_filtrados
        return redirect(url_for("menu_principal"))
    return render_template("filtro_consumo.html")

@app.route('/resultados')
def resultados():
    """
    Muestra los resultados de los autos filtrados y luego reinicia la lista de autos en la sesión.
    """
    autos = session.get("autos_filtrados", lista_autos)
    resultado = render_template("resultados.html", autos=autos)
    session["autos_filtrados"] = lista_autos
    return resultado

if __name__ == '__main__':
    app.run(debug=True)
