package com.ml.luisramirez.mltest

import android.content.Intent
import android.graphics.Bitmap
import android.support.v7.app.AppCompatActivity
import android.os.Bundle
import android.provider.MediaStore
import kotlinx.android.synthetic.main.activity_main.*
import android.R.attr.bitmap
import com.google.firebase.ml.vision.common.FirebaseVisionImage
import com.google.firebase.ml.vision.FirebaseVision
import com.google.firebase.ml.vision.text.FirebaseVisionTextRecognizer
import android.support.annotation.NonNull
import android.support.v7.widget.LinearLayoutManager
import android.support.v7.widget.RecyclerView
import com.google.android.gms.tasks.OnFailureListener
import com.google.firebase.ml.vision.text.FirebaseVisionText
import com.google.android.gms.tasks.OnSuccessListener
import com.google.firebase.ml.vision.text.RecognizedLanguage
import java.util.Arrays.asList
import com.google.firebase.ml.vision.text.FirebaseVisionCloudTextRecognizerOptions
import java.util.*
import kotlinx.android.synthetic.main.content_main.*



class MainActivity : AppCompatActivity() {
    val REQUEST_IMAGE_CAPTURE = 1;
    internal var rView: RecyclerView ?= null;
    internal var roma = arrayOf("ichi", "ni", "san", "yon");
    internal var mean = arrayOf("One", "Two", "Three", "Four");

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        btnTakePhoto.setOnClickListener{ dispatchTakePictureIntent() };
      
        rView = findViewById(R.id.rView) as RecyclerView;
        rView!!.setLayoutManager(LinearLayoutManager(this));
        rView!!.setAdapter(Adapter(this, roma));

    }

    private fun dispatchTakePictureIntent() {
        Intent(MediaStore.ACTION_IMAGE_CAPTURE).also { takePictureIntent ->
            takePictureIntent.resolveActivity(packageManager)?.also {
                startActivityForResult(takePictureIntent, REQUEST_IMAGE_CAPTURE)
            }
        }
    }
    override fun onActivityResult(requestCode: Int, resultCode: Int, data: Intent?) {
        if (requestCode == REQUEST_IMAGE_CAPTURE && resultCode == RESULT_OK) {
            val imageBitmap = data!!.extras.get("data") as Bitmap
            imgTaken.setImageBitmap(imageBitmap);
            val image = FirebaseVisionImage.fromBitmap(imageBitmap);

            val options = FirebaseVisionCloudTextRecognizerOptions.Builder()
                    .setLanguageHints(Arrays.asList("ja"))
                    .build();
            val textRecognizer = FirebaseVision.getInstance()
                    .getCloudTextRecognizer(options);

            textRecognizer.processImage(image)
                    .addOnSuccessListener {result ->
                        txtResult.text = result.text;
                        btnTakePhoto.text = result.text;
                    }
                    .addOnFailureListener {res ->
                        txtResult.text = res.message;
                    }

        }
    }
}
