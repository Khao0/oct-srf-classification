curl -X POST http://localhost:8000/single-line-predict \
    -F "retinal_fundus=@data/retinal_fundus.png" \
    -F "tomogram=@data/tomogram.png" \
    -o result.json