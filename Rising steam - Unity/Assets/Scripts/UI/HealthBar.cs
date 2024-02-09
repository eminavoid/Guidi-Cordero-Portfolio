using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;

public class HealthBar : MonoBehaviour
{
    [SerializeField] private Slider slider;
    [SerializeField] private GameObject attachedObj;

    private void SetMaxHealth()
    {
        if (attachedObj.TryGetComponent<Player>(out Player attachedP))
        {
            slider.maxValue = attachedP.maxlifePost();
            slider.value = attachedP.maxlifePost();
        }
        if (attachedObj.TryGetComponent<Enemy>(out Enemy attachedE))
        {
            slider.maxValue = attachedE.maxlifePost();
            slider.value = attachedE.maxlifePost();
        }
    }


    public void SetHealth()
    {
        if (attachedObj.TryGetComponent<Player>(out Player attachedP))
        {
            slider.value = attachedP.lifePost();
        }
        if (attachedObj.TryGetComponent<Enemy>(out Enemy attachedE))
        {
            slider.value = attachedE.lifePost();
        }
    }

    // Start is called before the first frame update
    void Start()
    {
        SetMaxHealth();
    }

    // Update is called once per frame
    void Update()
    {
        
    }
}
