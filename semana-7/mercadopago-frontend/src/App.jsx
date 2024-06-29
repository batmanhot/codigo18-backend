import { initMercadoPago, Wallet } from "@mercadopago/sdk-react";

// public key de tu cuenta creada en mercado pago
initMercadoPago("TEST-dd1339cf-0c47-4a4e-868e-c67e47ab6039");

export default function App() {
  return (
    <main className="max-w-lg m-auto">
      <section className="p-6">
        <h1 className="text-center text-2xl font-bold">
          Integrando Mercado Pago
        </h1>

        {/* <Wallet
          initialization={{
            // El id que se pone aqui "id": "1875332841-9ee4bfd2-91f6-44a6-b651-501819c0138e", es el que aparece luego de insertar una dato (POST) a travez del postman.

            preferenceId: "1875332841-27f1944e-9717-4b09-ae4e-91676df4c4c2",
          }}
        /> */}
        
        <CardPayment
          initialization={{ amount: 500 }}
          customization={{
            visual: {
              style: {
                theme: "flat",
              },
            },
            paymentMethods: {
              creditCard: "all",
              debitCard: "all",
              ticket: "all",
              bankTransfer: "all",
              onboarding_credits: "all",
              maxInstallments: 12,
            },
          }}
          onSubmit={async (param) => {
            const response = await fetch(
              "http://127.0.0.1:8000/api/v1/create-payment/",
              {
                method: "POST",
                headers: {
                  "Content-Type": "application/json",
                },
                body: JSON.stringify({
                  transaction_amount: param.transaction_amount,
                  token: param.token,
                  description: "Venta de S/500",
                  installments: param.installments,
                  payment_method_id: param.payment_method_id,
                  email: param.payer.email,
                  type: param.payer.identification.type,
                  number: param.payer.identification.number,
                }),
              }
            );
            const data = await response.json();
            console.log(data);
          }}
        /> 

      </section>
    </main>
  );
}