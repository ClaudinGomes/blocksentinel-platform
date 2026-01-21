from fastapi import FastAPI

app = FastAPI(
    title="BlockSentinel API",
    description="Risk analysis and intelligence for Web3 projects",
    version="0.1.0"
)

@app.get("/health")
def health_check():
    return {
        "status": "ok",
        "service": "BlockSentinel Backend"
    }
