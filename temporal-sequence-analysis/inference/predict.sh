URL="http://localhost:8000/temporal-sequence-predict"
ARGS=""

for i in {1..12}; do
    FILE="../data/preprocessed/radial/${i}.png"
    if [ -f "$FILE" ]; then
        ARGS="$ARGS -F radial_${i}=@$FILE"
    else
        echo "Missing $FILE"
    fi
done

for i in {1..25}; do
    FILE="../data/preprocessed/raster/${i}.png"
    if [ -f "$FILE" ]; then
        ARGS="$ARGS -F raster_${i}=@$FILE"
    else
        echo "Missing $FILE"
    fi
done

curl -X POST $URL $ARGS -o result.json