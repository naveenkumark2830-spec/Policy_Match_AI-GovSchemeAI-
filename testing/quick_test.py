from src.rag_engine import OptimizedRAGEngine

rag = OptimizedRAGEngine(r"C:\GovSchemeAI\GovSchemeAI")

queries = [
    "widow pension",
    "student scholarship",
    "farmer financial assistance",
    "job training unemployed",
    "senior citizen pension"
]

for q in queries:
    print("\n" + "="*80)
    print("QUERY:", q)

    results = rag.search(q, top_k=10)

    for r in results:
        print(
            f"ID={r['id']} | "
            f"SIM={r['similarity']} | "
            f"{r['scheme'][:120]}"
        )