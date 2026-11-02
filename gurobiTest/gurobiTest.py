import gurobipy as gp

try:
    with gp.Env() as env:
        with gp.Model(env=env) as model:
            print("\n" + "=" * 50)
            print("  GUROBI LIZENZ-STATUS CHECK")
            print("=" * 50)

            # Test-Modell mit Variablen erstellen
            v1 = model.addVar(name="x")
            v2 = model.addVar(name="y")
            model.addConstr(v1 + v2 <= 10)
            model.optimize()

            print("\n✅ Deine Lizenz ist AKTIV und einsatzbereit!")
            print("=" * 50)

except gp.GurobiError as e:
    print(f"\n❌ Gurobi-Fehler: {e}")