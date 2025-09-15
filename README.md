run: |
  curl -X POST "https://REGION-PROJECT.cloudfunctions.net/triggerNFT" \
    -H "Authorization: Bearer ${{ secrets.GCF_TOKEN }}" \
    -H "Content-Type: application/json" \
    -d '{"action":"mint_and_promote"}'# tokenla-nft-engine---
